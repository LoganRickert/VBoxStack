from fastapi import Body, FastAPI
from vbox import *

app = FastAPI()

@app.get("/")
def read_root():
    return {"alive": "true"}

@app.get("/v1/vms/ostypes")
def get_ostypes():
    vbs = VirtualBoxes()
    return {
        "ostypes": vbs.get_ostypes()
    }

@app.get("/v1/vms/running_vms")
def get_running_vms():
    vbs = VirtualBoxes()
    return {
        "vms": vbs.get_running_vms()
    }

@app.get("/v1/vms/vms")
def get_vms():
    vbs = VirtualBoxes()
    return {
        "vms": vbs.get_ostypes()
    }

@app.post("/v1/vm/delete")
def delete(vmid: str = Body(..., embed=True)):
    vb = VirtualBox(vmid)
    return {
        "message": vb.delete()
    }

@app.post("/v1/vm/clonevdi")
def clonevdi(vmid: str = Body(..., embed=True), input_path: str = Body(..., embed=True), output_path: str = Body(..., embed=True)):
    vb = VirtualBox(vmid)
    return {
        "message": vb.clonevdi(input_path, output_path)
    }

@app.post("/v1/vm/import")
def vm_import(vmid: str = Body(..., embed=True), input_path: str = Body(..., embed=True), name: str = Body(..., embed=True)):
    vb = VirtualBox(vmid)
    return {
        "message": vb.vm_import(input_path, name)
    }

@app.post("/v1/vm/export")
def vm_export(vmid: str = Body(..., embed=True), output_path: str = Body(..., embed=True)):
    vb = VirtualBox(vmid)
    return {
        "message": vb.vm_export(output_path)
    }

@app.post("/v1/vm/shutdown")
def shutdown(vmid: str = Body(..., embed=True), hard: bool = Body(..., embed=True)):
    vb = VirtualBox(vmid)
    return {
        "message": vb.shutdown(hard)
    }

@app.post("/v1/vm/reset")
def reset(vmid: str = Body(..., embed=True)):
    vb = VirtualBox(vmid)
    return {
        "message": vb.reset()
    }

@app.post("/v1/vm/resume")
def resume(vmid: str = Body(..., embed=True)):
    vb = VirtualBox(vmid)
    return {
        "message": vb.resume()
    }

@app.post("/v1/vm/pause")
def pause(vmid: str = Body(..., embed=True)):
    vb = VirtualBox(vmid)
    return {
        "message": vb.pause()
    }

@app.post("/v1/vm/start_headless")
def start_headless(vmid: str = Body(..., embed=True)):
    vb = VirtualBox(vmid)
    return {
        "message": vb.start_headless()
    }

@app.post("/v1/vm/vrde_address")
def vrde_address(vmid: str = Body(..., embed=True), address: str = Body(..., embed=True)):
    vb = VirtualBox(vmid)
    return {
        "message": vb.set_vrde_address(address)
    }

@app.post("/v1/vm/vrde_port")
def vrde_port(vmid: str = Body(..., embed=True), port: int = Body(..., embed=True)):
    vb = VirtualBox(vmid)
    return {
        "message": vb.set_vrde_port(port)
    }

@app.post("/v1/vm/vrde")
def vrde(vmid: str = Body(..., embed=True), on: bool = Body(..., embed=True), port: int = Body(..., embed=True), address: str = Body(..., embed=True)):
    vb = VirtualBox(vmid)
    return {
        "message": vb.set_vrde(on, port, address)
    }

@app.post("/v1/vm/attach_storage")
def attach_storage(vmid: str = Body(..., embed=True), controller: str = Body(..., embed=True), port: int = Body(..., embed=True), disk_type: str = Body(..., embed=True), path: str = Body(..., embed=True)):
    vb = VirtualBox(vmid)
    return {
        "message": vb.attach_storage(controller, port, disk_type, path)
    }

@app.post("/v1/vm/ide_controller")
def ide_controller(vmid: str = Body(..., embed=True)):
    vb = VirtualBox(vmid)
    return {
        "message": vb.create_ide_controller()
    }

@app.post("/v1/vm/sata_controller")
def sata_controller(vmid: str = Body(..., embed=True)):
    vb = VirtualBox(vmid)
    return {
        "message": vb.create_sata_controller()
    }

@app.post("/v1/vm/mac_address")
def mac_address(vmid: str = Body(..., embed=True), address_id: int = Body(..., embed=True), address: str = Body(..., embed=True)):
    vb = VirtualBox(vmid)
    return {
        "message": vb.set_mac_address(address_id, address)
    }

@app.post("/v1/vm/boot")
def boot(vmid: str = Body(..., embed=True), boot_id: int = Body(..., embed=True), device: str = Body(..., embed=True)):
    vb = VirtualBox(vmid)
    return {
        "message": vb.set_boot(boot_id, device)
    }

@app.post("/v1/vm/bridge_adapter")
def bridge_adapter(vmid: str = Body(..., embed=True), adapter_id: int = Body(..., embed=True), adapter: str = Body(..., embed=True)):
    vb = VirtualBox(vmid)
    return {
        "message": vb.set_bridge_adapter(adapter_id, adapter)
    }

@app.post("/v1/vm/nic")
def nic(vmid: str = Body(..., embed=True), nic_id: int = Body(..., embed=True), nic: str = Body(..., embed=True)):
    vb = VirtualBox(vmid)
    return {
        "message": vb.set_nic(nic_id, nic)
    }

@app.post("/v1/vm/acpi")
def acpi(vmid: str = Body(..., embed=True), on: bool = Body(..., embed=True)):
    vb = VirtualBox(vmid)
    return {
        "message": vb.set_acpi(on)
    }

@app.post("/v1/vm/ostype")
def ostype(vmid: str = Body(..., embed=True), ostype: str = Body(..., embed=True)):
    vb = VirtualBox(vmid)
    return {
        "message": vb.set_ostype(ostype)
    }

@app.post("/v1/vm/description")
def description(vmid: str = Body(..., embed=True), description: str = Body(..., embed=True)):
    vb = VirtualBox(vmid)
    return {
        "message": vb.set_description(description)
    }

@app.post("/v1/vm/memory")
def memory(vmid: str = Body(..., embed=True), memory: int = Body(..., embed=True)):
    vb = VirtualBox(vmid)
    return {
        "message": vb.set_memory(memory)
    }

@app.post("/v1/vm/cpus")
def cpus(vmid: str = Body(..., embed=True), cpus: int = Body(..., embed=True)):
    vb = VirtualBox(vmid)
    return {
        "message": vb.set_cpus(cpus)
    }

@app.post("/v1/vm/create")
def create(vmid: str = Body(..., embed=True)):
    vb = VirtualBox(vmid)
    return {
        "message": vb.create()
    }

@app.post("/v1/vm/create_hd")
def create_hd(vmid: str = Body(..., embed=True), path: str = Body(..., embed=True), size: int = Body(..., embed=True)):
    vb = VirtualBox(vmid)
    return {
        "message": vb.create_hd(path, size)
    }

