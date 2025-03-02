from data.connection_manager import ConnectionManager

def execute():
    connection_manager = ConnectionManager()
    return connection_manager.get_data_layer()
