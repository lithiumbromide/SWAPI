---
title: "eDAssembly Class"
project: ""
interface: "eDAssembly"
member: ""
kind: "class"
source: "emodeltoolkit/eDAssembly/eDAssembly_Class.htm"
---

# eDAssembly Class

| See Also | Example | Accessors | Availability |
| --- | --- | --- | --- |

Contains one or more parts and assemblies.

#### Header file code

```vb
class eDAssembly : public eDObject
{
public:

eDOutcome CreatePart( const ECHAR *partname, const eDAppearance &appearance, eDPart *& part ); //Creates a part

eDOutcome CreateSubAssembly( const ECHAR *assemblyname, const eDAppearance &appearance, eDAssembly *& assembly ); //Creates a subassembly

eDOutcome AddBody( const eDBody *body ); //Adds a body

};
```
