---
title: "Parameter Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "Parameter"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~Parameter.html"
---

# Parameter Method (IModelDoc2)

Gets the specified parameter.

## Syntax

### Visual Basic (Declaration)

```vb
Function Parameter( _
   ByVal StringIn As System.String _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim StringIn As System.String
Dim value As System.Object

value = instance.Parameter(StringIn)
```

### C#

```csharp
System.object Parameter(
   System.string StringIn
)
```

### C++/CLI

```cpp
System.Object^ Parameter(
   System.String^ StringIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `StringIn`: Name of parameter (for example, "D1@Base-Revolve")

### Return Value

Parameter (see **Remarks**)

## VBA Syntax

See [ModelDoc2::Parameter](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~Parameter.html).

## Examples

[Change Dimension (VBA)](Change_Dimension_Example_VB.htm)
[Get Depth of Extrusion (VBA)](Get_Depth_of_Extrusion_Example_VB.htm)
[Modify Plane By Changing System Value (VBA)](Modify_Plane_by_Changing_System_Value_Example_VB.htm)
[Recalculate Bounding Box (C#)](Recalculate_Bounding_Box_Example_CSharp.htm)
[Recalculate Bounding Box (VB.NET)](Recalculate_Bounding_Box_Example_VBNET.htm)
[Recalculate Bounding Box (VBA)](Recalculate_Bounding_Box_Example_VB.htm)

## Remarks

Most parameters are [dimensions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimension.html).

The StringIn argument must be the fully qualified dimension name (for example, "D1@Base-Extrude") for this method. However, the full dimension name is not needed if you use [IFeature::IParameter](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IParameter.html) or [IFeature::Parameter](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~Parameter.html).

Some characters are recognized as special characters. The use of these characters in names or parts or features can cause this method to fail to return a dimension. These special characters are not recognized in names of parts or features:

- at sign ( @ )
- period ( . )
- backslash ( / )

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::IParameter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IParameter.html)
[IModelDoc2::SetParamValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetParamValue.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
