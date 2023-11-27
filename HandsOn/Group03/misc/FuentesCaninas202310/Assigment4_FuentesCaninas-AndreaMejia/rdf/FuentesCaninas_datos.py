import morph_kgc
config = """
             [FuentesCaninas_data_graph]
             mappings:FuentesCaninas.rml.ttl
         """

g = morph_kgc.materialize(config)