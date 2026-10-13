---
title: "GetFaceColorFilter Method (IPowerSelect)"
project: "SOLIDWORKS Utilities API Help"
interface: "IPowerSelect"
member: "GetFaceColorFilter"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~GetFaceColorFilter.html"
---

# GetFaceColorFilter Method (IPowerSelect)

Gets the Face color filter set in this PowerSelect session.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFaceColorFilter( _
   ByRef Red As System.Double, _
   ByRef Green As System.Double, _
   ByRef Blue As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPowerSelect
Dim Red As System.Double
Dim Green As System.Double
Dim Blue As System.Double
Dim value As System.Integer

value = instance.GetFaceColorFilter(Red, Green, Blue)
```

### C#

```csharp
System.int GetFaceColorFilter(
   out System.double Red,
   out System.double Green,
   out System.double Blue
)
```

### C++/CLI

```cpp
System.int GetFaceColorFilter(
   [Out] System.double Red,
   [Out] System.double Green,
   [Out] System.double Blue
)
```

### Parameters

- `Red`: <=0.0 to <= 1.0
- `Green`: <=0.0 to <= 1.0
- `Blue`: <=0.0 to <= 1.0

### Return Value

Error as defined in [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

## VBA Syntax

See [IPowerSelect::GetFaceColorFilter](ms-its:swutilitiesapivb6.chm::/swutilities~IPowerSelect~GetFaceColorFilter.html).

## Examples

[Select and Get Number of Edges, Loops, Faces, and Features (VBA)](Select_and_Get_Number_of_Edges,_Loops,_Faces,_and_Features_Example_VB6.htm)

## See Also

[IPowerSelect Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect.html)
[IPowerSelect Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect_members.html)
[IPowerSelect::SetFaceColorFilter Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~SetFaceColorFilter.html)

## Availability

SOLIDWORKS Utilities API 2005 FCS
