---
title: "Components Property (ICavityFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICavityFeatureData"
member: "Components"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData~Components.html"
---

# Components Property (ICavityFeatureData)

Gets or sets the design components for this cavity.

## Syntax

### Visual Basic (Declaration)

```vb
Property Components As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICavityFeatureData
Dim value As System.Object

instance.Components = value

value = instance.Components
```

### C#

```csharp
System.object Components {get; set;}
```

### C++/CLI

```cpp
property System.Object^ Components {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of design [components](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html)

## VBA Syntax

See [CavityFeatureData::Components](ms-its:sldworksapivb6.chm::/sldworks~CavityFeatureData~Components.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[ICavityFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData.html)
[ICavityFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData_members.html)
[ICavityFeatureData::GetComponentsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData~GetComponentsCount.html)
[ICavityFeatureData::IGetComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData~IGetComponents.html)
[ICavityFeatureData::ISetComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData~ISetComponents.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13
