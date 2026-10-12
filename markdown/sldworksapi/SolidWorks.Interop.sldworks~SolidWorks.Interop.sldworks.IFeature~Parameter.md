---
title: "Parameter Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "Parameter"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Parameter.html"
---

# Parameter Method (IFeature)

Gets a pointer to the object for the specified parameter or a pointer to the specified parameter.

## Syntax

### Visual Basic (Declaration)

```vb
Function Parameter( _
   ByVal Name As System.String _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim Name As System.String
Dim value As System.Object

value = instance.Parameter(Name)
```

### C#

```csharp
System.object Parameter(
   System.string Name
)
```

### C++/CLI

```cpp
System.Object^ Parameter(
   System.String^ Name
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Name`: Name of parameter (for example, "D1")

### Return Value

Parameter (see **Remarks**)

## VBA Syntax

See [Feature::Parameter](ms-its:sldworksapivb6.chm::/sldworks~Feature~Parameter.html).

## Examples

[Change Dimension (VBA)](Change_Dimension_Example_VB.htm)
[Change Dimension (VB.NET)](Change_Dimension_Example_VBNET.htm)
[Change Dimension (C#)](Change_Dimension_Example_CSharp.htm)

## Remarks

Most parameters are [dimensions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimension.html).

The Name argument for this method does not have to be the "full" dimension name. For example, you only need to pass "D1" not "D1@Base-Revolve". The full dimension name is required if you call [IModelDoc2::Parameter](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~Parameter.html).

SOLIDWORKS recognizes some characters as special characters. The use of these characters in part or feature names can cause this method to fail and not return a dimension. These special characters are not recognized in names of parts or features:

- at sign ( @ )
- period ( . )
- backslash ( / )

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
[IFeature::IParameter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IParameter.html)
[ModelDoc2::IParameter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IParameter.html)
[IDimension::FullName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~FullName.html)
