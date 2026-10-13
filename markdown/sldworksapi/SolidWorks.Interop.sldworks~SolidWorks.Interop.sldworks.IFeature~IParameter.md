---
title: "IParameter Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "IParameter"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IParameter.html"
---

# IParameter Method (IFeature)

Gets a pointer to the object for the specified parameter or a pointer to the specified parameter.

## Syntax

### Visual Basic (Declaration)

```vb
Function IParameter( _
   ByVal Name As System.String _
) As Dimension
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim Name As System.String
Dim value As Dimension

value = instance.IParameter(Name)
```

### C#

```csharp
Dimension IParameter(
   System.string Name
)
```

### C++/CLI

```cpp
Dimension^ IParameter(
   System.String^ Name
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Name`: Name of parameter (for example, "D1")

### Return Value

[Dimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimension.html)

## VBA Syntax

See [Feature::IParameter](ms-its:sldworksapivb6.chm::/sldworks~Feature~IParameter.html).

## Remarks

Most parameters are [dimensions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimension.html).

The Name argument for this method does not have to be the "full" dimension name. For example, you only need to pass "D1" not "D1@Base-Revolve". The full dimension name is required if you call [IModelDoc2::IParameter](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IParameter.html).

SOLIDWORKS recognizes some characters as special characters. The use of these characters in part or feature names can cause this method to fail and not return a dimension. These special characters are not recognized in names of parts or features:

- at sign ( @ )
- period ( . )
- backslash ( / )

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
[IFeature::Parameter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Parameter.html)
[IModelDoc2::Parameter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~Parameter.html)
[IDimension::FullName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~FullName.html)
