---
title: "ContactComponents Property (ISimulation3DContactFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulation3DContactFeatureData"
member: "ContactComponents"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData~ContactComponents.html"
---

# ContactComponents Property (ISimulation3DContactFeatureData)

Gets or sets the components to check for contact in a 3D Contact feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ContactComponents As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulation3DContactFeatureData
Dim value As System.Object

instance.ContactComponents = value

value = instance.ContactComponents
```

### C#

```csharp
System.object ContactComponents {get; set;}
```

### C++/CLI

```cpp
property System.Object^ ContactComponents {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of [components](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html)

## VBA Syntax

See [Simulation3DContactFeatureData::ContactComponents](ms-its:sldworksapivb6.chm::/sldworks~Simulation3DContactFeatureData~ContactComponents.html).

## Examples

See the [ISimulation3DContactFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData.html) examples.

## See Also

[ISimulation3DContactFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData.html)
[ISimulation3DContactFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData_members.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
