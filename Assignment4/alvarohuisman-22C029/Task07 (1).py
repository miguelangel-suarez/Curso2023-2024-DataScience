#!/usr/bin/env python
# coding: utf-8

# **Task 07: Querying RDF(s)**

# In[1]:


get_ipython().system('pip install rdflib')
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2023-2024/master/Assignment4/course_materials"


# First let's read the RDF file

# In[20]:


from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
#g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
#g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example6.rdf", format="xml")
for s, p, o in g:
  print(s,p,o)


# **TASK 7.1: List all subclasses of "LivingThing" with RDFLib and SPARQL**

# In[3]:


# TO DO
from rdflib.plugins.sparql import prepareQuery
import rdflib
q1 = prepareQuery('''
  SELECT ?Subject WHERE { 
    ?Subject rdfs:subClassOf ?LivingThing. 
  }
  ''',
  initNs = { "rdfs": RDFS}
)

living = rdflib.URIRef("http://somewhere#LivingThing")
# Visualize the results

for r in g.query(q1, initBindings={'LivingThing':living}):
  print(r.Subject)


# **TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**
# 

# In[4]:


# TO DO
from rdflib import RDF

q21 = prepareQuery('''
  SELECT ?Subject WHERE { 
    ?Subject rdf:type ?Researcher.   
  }
  ''',
  initNs = {"rdf": RDF}
)
q22 = prepareQuery('''
  SELECT ?Subject WHERE { 
    ?Subject rdf:type ?Person.   
  }
  ''',
  initNs = {"rdf": RDF}
)
q23 = prepareQuery('''
  SELECT ?Subject WHERE { 
    ?Subject rdf:type ?Professor.   
  }
  ''',
  initNs = {"rdf": RDF}
)
q24 = prepareQuery('''
  SELECT ?Subject WHERE { 
    ?Subject rdf:type ?PhDstudent.   
  }
  ''',
  initNs = {"rdf": RDF}
)
person = rdflib.URIRef("http://somewhere#Person")
researcher = rdflib.URIRef("http://somewhere#Researcher")
professor = rdflib.URIRef("http://somewhere#Professor")
phdstudent = rdflib.URIRef("http://somewhere#PhDstudent")

# Visualize the results
for r in g.query(q21,initBindings={'Researcher': researcher}):
  print(r.Subject)
for r in g.query(q22,initBindings={'Person':person}):
  print(r.Subject)
for r in g.query(q23,initBindings={'Professor':professor}):
  print(r.Subject)
for r in g.query(q24,initBindings={'PhDstudent':phdstudent}):
  print(r.Subject)


# **TASK 7.3: List all individuals of "Person" or "Animal" and all their properties including their class with RDFLib and SPARQL. You do not need to list the individuals of the subclasses of person**
# 

# In[33]:


# TO DO

VCARD = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")
q31 = prepareQuery('''
  SELECT ?Subject ?Fullname ?Given ?Family WHERE { 
    ?Subject rdf:type  ?Person.
    ?Subject vcard:FN ?FullName.
    ?Subject vcard:Given ?Given.
    ?Subject vcard:Family ?Family.
    
    
  }
  ''',
  initNs = {"rdf": RDF, "vcard":VCARD}
)

# Visualize the results
for r in g.query(q31,initBindings={'Person':person}):
  print(r.Subject, r.FullName, r.Given)


q32 = prepareQuery('''
  SELECT ?Subject ?Fullname ?Given ?Family WHERE { 
    ?Subject rdf:type  ?Animal.
    ?Subject vcard:FN ?FullName.
    ?Subject vcard:Given ?Given.
    ?Subject vcard:Family ?Family.
    
  }
  ''',
  initNs = {"rdf": RDF, "vcard":VCARD}
)
animal = rdflib.URIRef("http://somewhere#Animal")
# Visualize the results
for r in g.query(q32,initBindings={'Animal':animal}):
  print(r.Subject, r.FullName, r.Given, r.Family)


# **TASK 7.4:  List the name of the persons who know Rocky**

# In[6]:


# TO DO
from rdflib import FOAF

q4 =  prepareQuery('''
  SELECT  ?Subject WHERE {
    ?Subject foaf:knows ?RockySmith.
    ?Subject rdf:type ?Person.
  }  
  ''',
  initNs = { "foaf": FOAF , "rdf": RDF}
)

rocky = rdflib.URIRef("http://somewhere#RockySmith")

# Visualize the results
for r in g.query(q4, initBindings={'RockySmith':rocky,'Person':person}):
    print(r.Subject)


# **Task 7.5: List the entities who know at least two other entities in the graph**

# In[7]:


# TO DO
# Visualize the results


# In[ ]:




