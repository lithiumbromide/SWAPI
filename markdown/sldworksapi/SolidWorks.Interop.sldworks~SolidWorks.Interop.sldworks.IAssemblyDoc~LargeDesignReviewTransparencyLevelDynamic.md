---
title: "LargeDesignReviewTransparencyLevelDynamic Property (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "LargeDesignReviewTransparencyLevelDynamic"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~LargeDesignReviewTransparencyLevelDynamic.html"
---

# LargeDesignReviewTransparencyLevelDynamic Property (IAssemblyDoc)

Gets or sets whether to dynamically modify the transparency level of unmodified components in the graphics area when the transparency level slider is moved on the Filter Modified Components PropertyManager page.

## Syntax

### Visual Basic (Declaration)

```vb
Property LargeDesignReviewTransparencyLevelDynamic As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim value As System.Boolean

instance.LargeDesignReviewTransparencyLevelDynamic = value

value = instance.LargeDesignReviewTransparencyLevelDynamic
```

### C#

```csharp
System.bool LargeDesignReviewTransparencyLevelDynamic {get; set;}
```

### C++/CLI

```cpp
property System.bool LargeDesignReviewTransparencyLevelDynamic {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to dynamically modify the transparency level of unmodified components in the graphics area when moving the transparency level slider, false to not

## VBA Syntax

See [AssemblyDoc::LargeDesignReviewTransparencyLevelDynamic](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~LargeDesignReviewTransparencyLevelDynamic.html).

## Examples

[Set Transparency of Components in Large Design Review (C#)](Set_Transparency_of_Components_LDR_Mode_Example_CSharp.htm)
[Set Transparency of Components in Large Design Review (VB.NET)](Set_Transparency_of_Components_LDR_Mode_Example_VBNET.htm)
[Set Transparency of Components in Large Design Review (VBA)](Set_Transparency_of_Components_LDR_Mode_Example_VB.htm)

## Remarks

This property is valid only when the assembly is opened in Large Design Review mode, and one or more of its components have been modified. When this property is enabled, modified components are opaque, and unmodified components change transparency as the transparency level slider moves.

The Filter Modified Components PropertyManager page appears when you click **Filter Modified Components** on the Large Design Review toolbar.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::LargeDesignReviewTransparencyLevel Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~LargeDesignReviewTransparencyLevel.html)
[IAssemblyDoc::LargeDesignReviewTransparencyLevelEnabled Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~LargeDesignReviewTransparencyLevelEnabled.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
