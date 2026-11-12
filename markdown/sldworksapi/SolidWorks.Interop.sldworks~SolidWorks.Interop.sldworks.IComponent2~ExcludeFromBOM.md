---
title: "ExcludeFromBOM Property (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "ExcludeFromBOM"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~ExcludeFromBOM.html"
---

# ExcludeFromBOM Property (IComponent2)

Obsolete. Superseded by [IComponent2::GetExcludeFromBOM2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetExcludeFromBOM2.html) and [IComponent2::SetExcludeFromBOM2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetExcludeFromBOM2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property ExcludeFromBOM As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim value As System.Boolean

instance.ExcludeFromBOM = value

value = instance.ExcludeFromBOM
```

### C#

```csharp
System.bool ExcludeFromBOM {get; set;}
```

### C++/CLI

```cpp
property System.bool ExcludeFromBOM {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to exclude this component from the BOM, false to include it

## VBA Syntax

See [Component2::ExcludeFromBOM](ms-its:sldworksapivb6.chm::/sldworks~Component2~ExcludeFromBOM.html).

## Remarks

This property applies to [table-based bills of materials](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature.html); it does not apply to Microsoft Excel-based bills of materials.

If you change this property to true, the name of the component in the FeatureManager design tree changes; (Excluded from BOM) is appended. To update the FeatureManager design tree, call [IFeatureManager::UpdateFeatureTree](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~UpdateFeatureTree.html).

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IAssemblyDoc::CompConfigProperties5 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CompConfigProperties5.html)

## Availability

SOLIDWORKS 2005 SP1, Revision Number 13.1
