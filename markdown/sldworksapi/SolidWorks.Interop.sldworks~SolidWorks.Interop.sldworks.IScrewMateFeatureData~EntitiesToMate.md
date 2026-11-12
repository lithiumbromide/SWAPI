---
title: "EntitiesToMate Property (IScrewMateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IScrewMateFeatureData"
member: "EntitiesToMate"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScrewMateFeatureData~EntitiesToMate.html"
---

# EntitiesToMate Property (IScrewMateFeatureData)

Gets or sets the entities to mate in this screw mate feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property EntitiesToMate As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IScrewMateFeatureData
Dim value As System.Object

instance.EntitiesToMate = value

value = instance.EntitiesToMate
```

### C#

```csharp
System.object EntitiesToMate {get; set;}
```

### C++/CLI

```cpp
property System.Object^ EntitiesToMate {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of two cylindrical [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html) of the two components to mate (see **Remarks**)

## VBA Syntax

See [ScrewMateFeatureData::EntitiesToMate](ms-its:sldworksapivb6.chm::/sldworks~ScrewMateFeatureData~EntitiesToMate.html).

## Examples

See the [IScrewMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScrewMateFeatureData.html) example.

## Remarks

Instead of specifying this property, you can use [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.html) to pre-select the entities to mate using Mark = 1 for each entity. You can pre-select mate entities during mate creation, but not during mate editing.

## See Also

[IScrewMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScrewMateFeatureData.html)
[IScrewMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScrewMateFeatureData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
