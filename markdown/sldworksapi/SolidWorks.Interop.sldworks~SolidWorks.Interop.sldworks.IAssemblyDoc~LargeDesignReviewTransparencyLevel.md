---
title: "LargeDesignReviewTransparencyLevel Property (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "LargeDesignReviewTransparencyLevel"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~LargeDesignReviewTransparencyLevel.html"
---

# LargeDesignReviewTransparencyLevel Property (IAssemblyDoc)

Gets or sets the transparency level of unmodified components in the graphics area of this assembly opened in Large Design Review mode.

## Syntax

### Visual Basic (Declaration)

```vb
Property LargeDesignReviewTransparencyLevel As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim value As System.Double

instance.LargeDesignReviewTransparencyLevel = value

value = instance.LargeDesignReviewTransparencyLevel
```

### C#

```csharp
System.double LargeDesignReviewTransparencyLevel {get; set;}
```

### C++/CLI

```cpp
property System.double LargeDesignReviewTransparencyLevel {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

0.0 (opaque) <= transparency level of unmodified components <= 1.0 (invisible)

## VBA Syntax

See [AssemblyDoc::LargeDesignReviewTransparencyLevel](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~LargeDesignReviewTransparencyLevel.html).

## Examples

[Set Transparency of Components in Large Design Review (C#)](Set_Transparency_of_Components_LDR_Mode_Example_CSharp.htm)
[Set Transparency of Components in Large Design Review (VB.NET)](Set_Transparency_of_Components_LDR_Mode_Example_VBNET.htm)
[Set Transparency of Components in Large Design Review (VBA)](Set_Transparency_of_Components_LDR_Mode_Example_VB.htm)

## Remarks

This property is valid only if all of the following are true:

- This assembly is opened in Large Design Review mode.
- One or more assembly components have been modified.
- [IAssemblyDoc::LargeDesignReviewTransparencyLevelEnabled](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~LargeDesignReviewTransparencyLevelEnabled.html) is set to true.

When transparency levels are enabled, modified components are opaque, and unmodified components have the transparency level specified by this property.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::LargeDesignReviewTransparencyLevelDynamic Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~LargeDesignReviewTransparencyLevelDynamic.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
