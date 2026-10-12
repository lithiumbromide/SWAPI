---
title: "Initialize Method (ISimpleFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISimpleFilletFeatureData2"
member: "Initialize"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~Initialize.html"
---

# Initialize Method (ISimpleFilletFeatureData2)

Initializes this simple fillet feature to the specified type.

## Syntax

### Visual Basic (Declaration)

```vb
Function Initialize( _
   ByVal FilletType As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleFilletFeatureData2
Dim FilletType As System.Integer
Dim value As System.Boolean

value = instance.Initialize(FilletType)
```

### C#

```csharp
System.bool Initialize(
   System.int FilletType
)
```

### C++/CLI

```cpp
System.bool Initialize(
   System.int FilletType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FilletType`: Simple fillet type as defined in [swSimpleFilletType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSimpleFilletType_e.html)

### Return Value

True if the simple fillet feature is initialized, false if not

## VBA Syntax

See [SimpleFilletFeatureData2::Initialize](ms-its:sldworksapivb6.chm::/sldworks~SimpleFilletFeatureData2~Initialize.html).

## Examples

See the [IPartialEdgeFilletData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData.html) and [ISimpleFilletFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.html) introductory examples.

## Remarks

After you initialize this data object with a fillet type, you need to narrow the fillet type by specifying [ISimpleFilletFeatureData2::ConicTypeForCrossSectionProfile](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~ConicTypeForCrossSectionProfile.html).

## See Also

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.html)
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
