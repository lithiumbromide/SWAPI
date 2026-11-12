---
title: "Accessing Attributes Imported from ACIS SAT Files"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Overview/Accessing_Attributes_Imported_from_ACIS_SAT_Files.htm"
---

# Accessing Attributes Imported from ACIS SAT Files

After an SAT file containing generic attributes has been imported into the SOLIDWORKS Design application, the attributes are imported as SOLIDWORKS attributes. You can access these attributes using the standard SOLIDWORKS attribute methods and properties.

The names of the attribute definitions are:

```vb
XLTR_ATTRIBUTE_DEFINITION_DOUBLE_TYPE for ATTRIB_GEN_REAL
XLTR_ATTRIBUTE_DEFINITION_STRING_TYPE for ATTRIB_GEN_STRING
XLTR_ATTRIBUTE_DEFINITION_INTEGER_TYPE for ATTRIB_GEN_INTEGER
XLTR_ATTRIBUTE_DEFINITION_DVECTOR_TYPE for ATTRIB_GEN_POSITION & ATTRIB_GEN_VECTOR
```

Each attribute definition has two parameters:

- Value. This parameter is of type swParamTypeString. It is of type swParamTypeDouble, swParamTypeString, swParamTypeInteger or swParamTypeDVector, depending on the attribute previously listed definitions.
- Name. The data contained in the Name parameter is the name of the attribute as defined in ACIS and the Value parameter contains the actual data in the attribute.
