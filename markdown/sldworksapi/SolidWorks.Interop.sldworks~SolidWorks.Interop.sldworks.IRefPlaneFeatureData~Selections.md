---
title: "Selections Property (IRefPlaneFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IRefPlaneFeatureData"
member: "Selections"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~Selections.html"
---

# Selections Property (IRefPlaneFeatureData)

Gets or sets the selected entities used to create the reference plane feature or sets the entities to use to create the reference plane feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Selections As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IRefPlaneFeatureData
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

See [RefPlaneFeatureData::Selections](ms-its:sldworksapivb6.chm::/sldworks~RefPlaneFeatureData~Selections.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

**IMPORTANT:** Reference planes created in SOLIDWORKS 2010 or later are constraint based; reference planes created in SOLIDWORKS 2009 or earlier are not. See the **Remarks** section in the [IRefPlaneFeatureData interface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRefPlaneFeatureData.html) topic for details about reference planes and this interface.

## See Also

[IRefPlaneFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData.html)
[IRefPlaneFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData_members.html)
[IRefPlaneFeatureData::GetSelectionsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~GetSelectionsCount.html)
[IRefPlaneFeatureData::IGetSelections Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~IGetSelections.html)
[IRefPlaneFeatureData::ISetSelections Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~ISetSelections.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
