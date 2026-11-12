---
title: "CreateBreakOutSection Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "CreateBreakOutSection"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateBreakOutSection.html"
---

# CreateBreakOutSection Method (IDrawingDoc)

Creates a broken-out section in a drawing document.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateBreakOutSection( _
   ByVal Depth As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim Depth As System.Double
Dim value As System.Boolean

value = instance.CreateBreakOutSection(Depth)
```

### C#

```csharp
System.bool CreateBreakOutSection(
   System.double Depth
)
```

### C++/CLI

```cpp
System.bool CreateBreakOutSection(
   System.double Depth
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Depth`: Depth of the broken-out section

### Return Value

True if the broken-out section was created, false if not

## VBA Syntax

See [DrawingDoc::CreateBreakOutSection](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~CreateBreakOutSection.html).

## Examples

[Create Broken-Out Section (VBA)](Create_BreakOut_Section_Example_VB.htm)
[Create Broken-Out Section (VB.NET)](Create_BreakOut_Section_Example_VBNET.htm)
[Create Broken-Out Section (C#)](Create_BreakOut_Section_Example_CSharp.htm)

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::CreateSectionViewAt4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateSectionViewAt4.html)
[IDrawingDoc::ICreateSectionViewAt4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateSectionViewAt4.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
