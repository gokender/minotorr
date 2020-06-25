from minotor import hardwaremonitor

comp = hardwaremonitor.HardwareMonitor()

print(comp.cpu.cores)
print(comp.cpu.temperatures)


print(comp.ram.loads)
print(comp.ram.data)

print(comp.ram.to_dict())
