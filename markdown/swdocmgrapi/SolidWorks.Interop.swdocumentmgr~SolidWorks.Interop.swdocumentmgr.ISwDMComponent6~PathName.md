---
title: "PathName Property (ISwDMComponent6)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMComponent6"
member: "PathName"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent6~PathName.html"
---

# PathName Property (ISwDMComponent6)

Gets the path for this component.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property PathName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMComponent6
Dim value As System.String

value = instance.PathName
```

### C#

```csharp
System.string PathName {get;}
```

### C++/CLI

```cpp
property System.String^ PathName {
   System.String^ get();
}
```

### Property Value

Path

## VBA Syntax

See [SwDMComponent6::PathName](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMComponent6~PathName.html).

## Examples

[Get Current Name of Configuration of Suppressed Component (C#)](Get_Current_Name_of_Configuration_of_Suppressed_Component_Example_CSharp.htm)
[Get Current Name of Configuration of Suppressed Component (VB.NET)](Get_Current_Name_of_Configuration_of_Suppressed_Component_Example_VBNET.htm)

## See Also

[ISwDMComponent6 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent6.html)
[ISwDMComponent6 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent6_members.html)

## Availability

SOLIDWORKS Document Manager API 2009 SP0
