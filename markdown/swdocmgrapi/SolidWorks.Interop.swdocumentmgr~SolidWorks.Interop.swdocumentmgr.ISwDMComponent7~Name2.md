---
title: "Name2 Property (ISwDMComponent7)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMComponent7"
member: "Name2"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent7~Name2.html"
---

# Name2 Property (ISwDMComponent7)

Obsolete. Superseded by [ISwDMComponent11::Name3](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent11~Name3.html).

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Name2 As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMComponent7
Dim value As System.String

value = instance.Name2
```

### C#

```csharp
System.string Name2 {get;}
```

### C++/CLI

```cpp
property System.String^ Name2 {
   System.String^ get();
}
```

### Property Value

Name of the component appended with an index value

## VBA Syntax

See [SwDMComponent7::Name2](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMComponent7~Name2.html).

## Examples

[Get Current Name of Configuration of Suppressed Component (VB.NET)](Get_Current_Name_of_Configuration_of_Suppressed_Component_Example_VBNET.htm)
[Get Current Name of Configuration of Suppressed Component (C#)](Get_Current_Name_of_Configuration_of_Suppressed_Component_Example_CSharp.htm)

## Remarks

This property returns the component name appended with an index in the format, "component-1".

## See Also

[ISwDMComponent7 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent7.html)
[ISwDMComponent7 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent7_members.html)
[ISwDMComponent7::SelectName Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent7~SelectName.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
