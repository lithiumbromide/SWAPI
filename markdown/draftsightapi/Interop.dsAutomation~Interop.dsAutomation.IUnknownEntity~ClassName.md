---
title: "ClassName Property (IUnknownEntity)"
project: ""
interface: "IUnknownEntity"
member: "ClassName"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IUnknownEntity~ClassName.html"
---

# ClassName Property (IUnknownEntity)

Gets the unique identifier of this unknown entity.

## Syntax

### Visual Basic

```vb
ReadOnly Property ClassName As System.String
```

### C#

```csharp
System.string ClassName {get;}
```

### JScript

```
function get ClassName : System.String
```

### Managed Extensions for C++

```
__property System.string* get_ClassName();
```

### C++/CLI

```cpp
property System.String^ ClassName {
   System.String^ get();
}
```

### Property Value

Class name or unique identifier

## Remarks

Use this property to uniquely identify this unknown entity that surfaces in one or more events:

[_IDocumentEvents_ObjectAppendNotify](Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_ObjectAppendNotifyEventHandler.html)

[_IDocumentEvents_ObjectEraseNotify](Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_ObjectEraseNotifyEventHandler.html)

[_IDocumentEvents_ObjectModifyNotify](Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_ObjectModifyNotifyEventHandler.html)

## See Also

[IUnknownEntity Interface](Interop.dsAutomation~Interop.dsAutomation.IUnknownEntity.html)
[IUnknownEntity Members](Interop.dsAutomation~Interop.dsAutomation.IUnknownEntity_members.html)

## Availability

DraftSight 2018 SP2
