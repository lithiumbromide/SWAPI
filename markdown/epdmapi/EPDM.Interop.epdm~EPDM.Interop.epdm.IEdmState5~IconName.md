---
title: "IconName Property (IEdmState5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmState5"
member: "IconName"
kind: "property"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmState5~IconName.html"
---

# IconName Property (IEdmState5)

Gets the name of the icon used in the workflow graph.

## Syntax

### Visual Basic

```vb
ReadOnly Property IconName As System.String
```

### C#

```csharp
System.string IconName {get;}
```

### C++/CLI

```cpp
property System.String^ IconName {
   System.String^ get();
}
```

### Property Value

Name of the icon

## Remarks

You can extract the icon from the **WfIcons.dll**, where the resource ID is the name stored in this property appended by "_SML".

## See Also

[IEdmState5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmState5.html)
[IEdmState5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmState5_members.html)
