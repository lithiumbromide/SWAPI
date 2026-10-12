---
title: "EnablePartialEdgeParameters Property (ISimpleFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISimpleFilletFeatureData2"
member: "EnablePartialEdgeParameters"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~EnablePartialEdgeParameters.html"
---

# EnablePartialEdgeParameters Property (ISimpleFilletFeatureData2)

Gets or sets whether to enable partial edge properties for all edges of this fillet.

## Syntax

### Visual Basic (Declaration)

```vb
Property EnablePartialEdgeParameters As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleFilletFeatureData2
Dim value As System.Boolean

instance.EnablePartialEdgeParameters = value

value = instance.EnablePartialEdgeParameters
```

### C#

```csharp
System.bool EnablePartialEdgeParameters {get; set;}
```

### C++/CLI

```cpp
property System.bool EnablePartialEdgeParameters {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to enable partial edge properties for all edges, false to not

## VBA Syntax

See [SimpleFilletFeatureData2::EnablePartialEdgeParameters](ms-its:sldworksapivb6.chm::/sldworks~SimpleFilletFeatureData2~EnablePartialEdgeParameters.html).

## Examples

See the [IPartialEdgeFilletData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData.html) example.

## See Also

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.html)
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
