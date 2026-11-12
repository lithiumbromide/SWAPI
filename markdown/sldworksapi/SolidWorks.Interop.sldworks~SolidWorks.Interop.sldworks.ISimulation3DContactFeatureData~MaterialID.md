---
title: "MaterialID Property (ISimulation3DContactFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulation3DContactFeatureData"
member: "MaterialID"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData~MaterialID.html"
---

# MaterialID Property (ISimulation3DContactFeatureData)

Gets or sets the type of material the specified component in this 3D Contact feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property MaterialID( _
   ByVal WhichOne As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulation3DContactFeatureData
Dim WhichOne As System.Integer
Dim value As System.Integer

instance.MaterialID(WhichOne) = value

value = instance.MaterialID(WhichOne)
```

### C#

```csharp
System.int MaterialID(
   System.int WhichOne
) {get; set;}
```

### C++/CLI

```cpp
property System.int MaterialID {
   System.int get(System.int WhichOne);
   void set (System.int WhichOne, System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `WhichOne`: 0-based index of the contact component

### Property Value

Material as defined by [swCosmosWorksMat](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCosmosWorksMat.html)

## VBA Syntax

See [Simulation3DContactFeatureData::MaterialID](ms-its:sldworksapivb6.chm::/sldworks~Simulation3DContactFeatureData~MaterialID.html).

## Examples

See the [ISimulation3DContactFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData.html) examples.

## Remarks

Available only when [ISimulation3DContactFeatureData::SpecifyMaterial](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimulation3DContactFeatureData~SpecifyMaterial.html) is true.

## See Also

[ISimulation3DContactFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData.html)
[ISimulation3DContactFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData_members.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
