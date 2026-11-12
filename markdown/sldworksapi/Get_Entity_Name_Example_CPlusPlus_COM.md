---
title: "Get Entity Name Example (C++ COM)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Entity_Name_Example_CPlusPlus_COM.htm"
---

# Get Entity Name Example (C++ COM)

This example shows how to get the name of the IEntity object.

```vb
BSTR entityName;
res = m_PartDoc->IGetEntityName(m_Entity, &entityName);

CString message;
message.Format(_T("Entity Name is: \t%s"), entityName);
AfxMessageBox( message );

SysFreeString(entityName);
```
