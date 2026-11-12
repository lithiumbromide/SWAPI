---
title: "SetFaceColorFilter Method (IPowerSelect)"
project: "SOLIDWORKS Utilities API Help"
interface: "IPowerSelect"
member: "SetFaceColorFilter"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~SetFaceColorFilter.html"
---

# SetFaceColorFilter Method (IPowerSelect)

Sets the Face color filter for this PowerSelect session.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetFaceColorFilter( _
   ByVal Red As System.Double, _
   ByVal Green As System.Double, _
   ByVal Blue As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPowerSelect
Dim Red As System.Double
Dim Green As System.Double
Dim Blue As System.Double
Dim value As System.Integer

value = instance.SetFaceColorFilter(Red, Green, Blue)
```

### C#

```csharp
System.int SetFaceColorFilter(
   System.double Red,
   System.double Green,
   System.double Blue
)
```

### C++/CLI

```cpp
System.int SetFaceColorFilter(
   System.double Red,
   System.double Green,
   System.double Blue
)
```

### Parameters

- `Red`: <=0.0 to <= 1.0
- `Green`: <=0.0 to <= 1.0
- `Blue`: <=0.0 to <= 1.0

### Return Value

Error as defined in [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

## VBA Syntax

See [IPowerSelect::SetFaceColorFilter](ms-its:swutilitiesapivb6.chm::/swutilities~IPowerSelect~SetFaceColorFilter.html).

## Examples

[Select and Get Number of Edges, Loops, Faces, and Features (VBA)](Select_and_Get_Number_of_Edges,_Loops,_Faces,_and_Features_Example_VB6.htm)

## See Also

[IPowerSelect Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect.html)
[IPowerSelect Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect_members.html)
[IPowerSelect::GetFaceColorFilter Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~GetFaceColorFilter.html)

## Availability

SOLIDWORKS Utilities API 2005 FCS
