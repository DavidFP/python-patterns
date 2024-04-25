from singleton.logger import Logger

if __name__=="__main__":
    objeto1 = Logger()
    objeto2 = Logger()
    
    print(f"Instancia objeto1: {objeto1._instanceName}")
    print(f"Instancia objeto2: {objeto2._instanceName}")
    
    objeto1.log_info("Mensaje desde objeto1")
    objeto2.log_warning("Warning desde objeto 2")
    objeto1.log_error("Error desde objeto 1")