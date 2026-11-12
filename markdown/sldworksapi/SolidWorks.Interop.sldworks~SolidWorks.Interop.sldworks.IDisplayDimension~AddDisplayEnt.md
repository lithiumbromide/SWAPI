---
title: "AddDisplayEnt Method (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "AddDisplayEnt"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~AddDisplayEnt.html"
---

# AddDisplayEnt Method (IDisplayDimension)

Overrides the display graphics of objects.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddDisplayEnt( _
   ByVal Type As System.Integer, _
   ByVal Data As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim Type As System.Integer
Dim Data As System.Object
Dim value As System.Boolean

value = instance.AddDisplayEnt(Type, Data)
```

### C#

```csharp
System.bool AddDisplayEnt(
   System.int Type,
   System.object Data
)
```

### C++/CLI

```cpp
System.bool AddDisplayEnt(
   System.int Type,
   System.Object^ Data
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Type`: Type of graphical entity (see **Remarks**)
- `Data`: Geometric data describing the entity (see **Remarks**)

### Return Value

True if successful, false if not

## VBA Syntax

See [DisplayDimension::AddDisplayEnt](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~AddDisplayEnt.html).

## Examples

[Replace Dimension with Text (VBA)](Replace_Dimension_with_Text_Example_VB.htm)

## Remarks

The new graphics displayed by this method are temporary. When the user changes the dimension, this display dimension reverts back to the SOLIDWORKS standard.

The type controls which geometry is added and what information is placed in the data array. All colors and line styles are taken from DisplayDimension.

| type | Description | data |
| --- | --- | --- |
| 1 | Line | 6 doubles; (x, y, z) start point and (x, y, z) end point |
| 2 | Filled triangle | 9 doubles; 3 (x, y, z) points of the triangle to fill |
| 3 | Filled 4 sided polygon | 12 doubles; 4 (x, y, z) points of the polygon to fill |
| 4 | Arc | 12 doubles; (x, y, z) center point, (x, y, z) normal vector, (x, y, z) start point and (x, y, z) end point |
| 5 | Circle | 7 doubles; (x, y, z) center point, (x, y, z) normal vector and radius |
| 6 | Filled dot | 4 doubles; (x, y, z) center point and radius |

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDisplayDimension::IAddDisplayText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~IAddDisplayText.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
