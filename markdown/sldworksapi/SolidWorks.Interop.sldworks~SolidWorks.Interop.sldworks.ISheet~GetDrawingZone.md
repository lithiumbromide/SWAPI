---
title: "GetDrawingZone Method (ISheet)"
project: "SOLIDWORKS API Help"
interface: "ISheet"
member: "GetDrawingZone"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetDrawingZone.html"
---

# GetDrawingZone Method (ISheet)

Gets the name of the drawing zone for the specified x and y coordinates on the sheet.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDrawingZone( _
   ByVal X As System.Double, _
   ByVal Y As System.Double _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISheet
Dim X As System.Double
Dim Y As System.Double
Dim value As System.String

value = instance.GetDrawingZone(X, Y)
```

### C#

```csharp
System.string GetDrawingZone(
   System.double X,
   System.double Y
)
```

### C++/CLI

```cpp
System.String^ GetDrawingZone(
   System.double X,
   System.double Y
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X`: x coordinate
- `Y`: y coordinate

### Return Value

Name of the drawing zone

## VBA Syntax

See [Sheet::GetDrawingZone](ms-its:sldworksapivb6.chm::/sldworks~Sheet~GetDrawingZone.html).

## Examples

[Get Name of Drawing Zone (C#)](Get_Name_of_Drawing_Zone_Example_CSharp.htm)
[Get Name of Drawing Zone (VB.NET)](Get_Name_of_Drawing_Zone_Example_VBNET.htm)
[Get Name of Drawing Zone (VBA)](Get_Name_of_Drawing_Zone_Example_VB.htm)

## See Also

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.html)
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.html)
[IDrawingDoc::NewSheet4 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~NewSheet4.html)
[IDrawingDoc::SetupSheet6 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SetupSheet6.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
