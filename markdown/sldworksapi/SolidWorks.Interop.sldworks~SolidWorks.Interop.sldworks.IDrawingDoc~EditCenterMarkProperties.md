---
title: "EditCenterMarkProperties Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "EditCenterMarkProperties"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~EditCenterMarkProperties.html"
---

# EditCenterMarkProperties Method (IDrawingDoc)

Edits center mark properties.

## Syntax

### Visual Basic (Declaration)

```vb
Sub EditCenterMarkProperties( _
   ByVal Angle As System.Double, _
   ByVal Size As System.Double, _
   ByVal Lines As System.Boolean, _
   ByVal DocSettings As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim Angle As System.Double
Dim Size As System.Double
Dim Lines As System.Boolean
Dim DocSettings As System.Boolean

instance.EditCenterMarkProperties(Angle, Size, Lines, DocSettings)
```

### C#

```csharp
void EditCenterMarkProperties(
   System.double Angle,
   System.double Size,
   System.bool Lines,
   System.bool DocSettings
)
```

### C++/CLI

```cpp
void EditCenterMarkProperties(
   System.double Angle,
   System.double Size,
   System.bool Lines,
   System.bool DocSettings
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Angle`: New angle of the center mark
- `Size`: New size of the center mark
- `Lines`: True displays the center mark lines, false displays the plus sign (+) at the circle
  center
- `DocSettings`: True uses the default settings for this document, false does not

## VBA Syntax

See [DrawingDoc::EditCenterMarkProperties](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~EditCenterMarkProperties.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[ICenterMark Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
