---
title: "EntitiesToMate Property (ILockMateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILockMateFeatureData"
member: "EntitiesToMate"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILockMateFeatureData~EntitiesToMate.html"
---

# EntitiesToMate Property (ILockMateFeatureData)

Gets or sets the entities to mate in this lock mate.

## Syntax

### Visual Basic (Declaration)

```vb
Property EntitiesToMate As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ILockMateFeatureData
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

Array of entities to mate (see **Remarks**)

## VBA Syntax

See [LockMateFeatureData::EntitiesToMate](ms-its:sldworksapivb6.chm::/sldworks~LockMateFeatureData~EntitiesToMate.html).

## Examples

See the [ILockMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILockMateFeatureData.html) example.

## Remarks

Instead of specifying this property, you can use [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.html) to pre-select the entities to mate using Mark = 1. You can pre-select mate entities during mate creation, but not during mate editing.

## See Also

[ILockMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILockMateFeatureData.html)
[ILockMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILockMateFeatureData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
