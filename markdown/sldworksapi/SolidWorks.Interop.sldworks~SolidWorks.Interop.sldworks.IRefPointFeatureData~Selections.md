---
title: "Selections Property (IRefPointFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IRefPointFeatureData"
member: "Selections"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPointFeatureData~Selections.html"
---

# Selections Property (IRefPointFeatureData)

Gets the entities selected to create the reference point or sets the entities to create the reference point.

## Syntax

### Visual Basic (Declaration)

```vb
Property Selections As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IRefPointFeatureData
Dim value As System.Object

instance.Selections = value

value = instance.Selections
```

### C#

```csharp
System.object Selections {get; set;}
```

### C++/CLI

```cpp
property System.Object^ Selections {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of selected entities

## VBA Syntax

See [RefPointFeatureData::Selections](ms-its:sldworksapivb6.chm::/sldworks~RefPointFeatureData~Selections.html).

## Examples

See [IRefPointFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRefPointFeatureData.html) examples.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IRefPointFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPointFeatureData.html)
[IRefPointFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPointFeatureData_members.html)
[IRefPointFeatureData::GetSelectionsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPointFeatureData~GetSelectionsCount.html)
[IRefPointFeatureData::IGetSelections Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPointFeatureData~IGetSelections.html)
[IRefPointFeatureData::ISetSelections Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPointFeatureData~ISetSelections.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
