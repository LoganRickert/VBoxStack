
import subprocess


class VirtualBox:

    vm_id = None

    def __init__(self, vm_id=None):
        self.vm_id = vm_id

    def _run_vbox_cmd(self, cmd, args=[]):
        try:
            results = subprocess.check_output([
                "VBoxManage", cmd
            ] + args, stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as e:
            print(e.output)
            return e.output

        r = results.decode("utf-8")
        return r

    def _run_modifyvm(self, args):
        return self._run_vbox_cmd("modifyvm", [
            self.vm_id
        ] + args)

    def _run_storagectl(self, args):
        return self._run_vbox_cmd("storagectl", [
            self.vm_id
        ] + args)

    def _run_controlvm(self, args):
        return self._run_vbox_cmd("controlvm", [
            self.vm_id
        ] + args)

    def _run_storageattach(self, args):
        return self._run_vbox_cmd("storageattach", [
            self.vm_id
        ] + args)

    def _run_startvm(self, args=[]):
        return self._run_vbox_cmd("startvm", [
            self.vm_id
        ] + args)

    def create_hd(self, path, size):
        return self._run_vbox_cmd("createhd", [
            "--filename", self.vm_id, "--size", str(size)
        ])

    def create(self):
        return self._run_vbox_cmd("createvm", [
            "--name", self.vm_id, "--register"
        ])

    def set_cpus(self, count):
        return self._run_modifyvm([
            "--cpus", str(count)
        ])

    def set_memory(self, memory):
        return self._run_modifyvm([
            "--memory", str(memory)
        ])

    def set_ioapic(self, on):
        return self._run_modifyvm([
            "--ioapic", "on" if on else "off"
        ])

    def set_description(self, description):
        return self._run_modifyvm([
            "--description", str(description)
        ])

    def set_ostype(self, ostype):
        return self._run_modifyvm([
            "--ostype", str(ostype)
        ])

    def set_acpi(self, on=True):
        return self._run_modifyvm([
            "--acpi", "on" if on else "off"
        ])

    def set_nic(self, nic_id=1, nic="bridged"):
        return self._run_modifyvm([
            "--nic" + str(nic_id), nic
        ])

    def set_bridge_adapter(self, adapter_id=1, adapter="enp3s0f0"):
        return self._run_modifyvm([
            "--bridgeadapter" + str(adapter_id), adapter
        ])

    def set_boot(self, boot_id=1, device="dvd"):
        return self._run_modifyvm([
            "--boot" + str(boot_id), device
        ])

    def set_mac_address(self, address_id=1, address="auto"):
        return self._run_modifyvm([
            "--macaddress" + str(address_id), address
        ])

    def create_sata_controller(self):
        return self._run_storagectl([
            "--name", "SATA Controller", "--add", "SATA"
        ])

    def create_ide_controller(self):
        return self._run_storagectl([
            "--name", "IDE Controller", "--add", "ide"
        ])

    def attach_storage(self, controller, port, disk_type, path):
        return self._run_storageattach([
            "--storagectl", controller, "--port", str(port), "--device", "0", "--type", disk_type, "--medium", path
        ])

    def set_vrde(self, on, port, address="0.0.0.0"):
        on = "on" if on else "off"
        return self._run_modifyvm([
            "--vrde", on, "--vrdeport", str(port), "--vrdeaddress", address, "--vrdemulticon", "on", "--vrdereusecon", "on", "--vrdeauthtype", "null"
        ])

    def set_vrde_port(self, port):
        return self._run_modifyvm([
            "--vrdeport", str(port)
        ])

    def set_vrde_address(self, address):
        return self._run_modifyvm([
            "--vrdeaddress", address
        ])

    def start_headless(self):
        return self._run_startvm([
            "--type", "headless"
        ])

    def pause(self):
        return self._run_controlvm([
            "pause"
        ])

    def resume(self):
        return self._run_controlvm([
            "resume"
        ])

    def reset(self):
        return self._run_controlvm([
            "reset"
        ])

    def shutdown(self, hard=False):
        hard = "hard" if hard else "soft"
        return self._run_controlvm([
            "poweroff", hard
        ])

    def vm_export(self, output_path):
        return self._run_vbox_cmd("export", [
            "-o", output_path + ".ova"
        ])

    def vm_import(self, input_path, vm_name):
        return self._run_vbox_cmd("import", [
            input_path, "--vsys", "0", "--vmname", vm_name
        ])

    def clonevdi(self, input_path, output_path):
        return self._run_vbox_cmd("clonevdi", [
            input_path, output_path
        ])

    def delete(self):
        return self._run_vbox_cmd("unregistervm", [
            "--delete", self.vm_id
        ])


class VirtualBoxes:

    def __init__(self):
        pass

    def _run_vbox_cmd(self, cmd, args=[]):
        try:
            results = subprocess.check_output([
                "VBoxManage", cmd
            ] + args, stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as e:
            print(e.output)
            return e.output

        r = results.decode("utf-8")
        return r

    def get_vms(self):
        r = self._run_vbox_cmd("list", ["vms"]).splitlines()
        return [
            ("\"".join(line.split("\"")[1:-1]),
             line.split("{")[-1][:-1])
            for line in r
        ]

    def get_running_vms(self):
        r = self._run_vbox_cmd("list", ["runningvms"]).splitlines()
        return [
            ("\"".join(line.split("\"")[1:-1]),
             line.split("{")[-1][:-1])
            for line in r
        ]

    def get_ostypes(self):
        r = self._run_vbox_cmd("list", ["ostypes"]).split("\n\n")
        return [
            [
                list(map(lambda l: l.strip(), line.split(":")))
                for line in ostype.splitlines()
            ]
            for ostype in r
        ][:-1]
