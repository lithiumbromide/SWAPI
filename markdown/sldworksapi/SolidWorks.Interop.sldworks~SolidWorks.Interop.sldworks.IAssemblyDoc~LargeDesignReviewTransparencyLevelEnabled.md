---
title: "LargeDesignReviewTransparencyLevelEnabled Property (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "LargeDesignReviewTransparencyLevelEnabled"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~LargeDesignReviewTransparencyLevelEnabled.html"
---

# LargeDesignReviewTransparencyLevelEnabled Property (IAssemblyDoc)

Gets or sets whether transparency levels are activated for unmodified components in the graphics area for this assembly opened in Large Design Review mode.

## Syntax

### Visual Basic (Declaration)

```vb
Property LargeDesignReviewTransparencyLevelEnabled As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim value As System.Boolean

instance.LargeDesignReviewTransparencyLevelEnabled = value

value = instance.LargeDesignReviewTransparencyLevelEnabled
```

### C#

```csharp
System.bool LargeDesignReviewTransparencyLevelEnabled {get; set;}
```

### C++/CLI

```cpp
property System.bool LargeDesignReviewTransparencyLevelEnabled {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if transparency levels are activated, false if not

## VBA Syntax

See [AssemblyDoc::LargeDesignReviewTransparencyLevelEnabled](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~LargeDesignReviewTransparencyLevelEnabled.html).

## Examples

[Set Transparency of Components in Large Design Review (C#)](Set_Transparency_of_Components_LDR_Mode_Example_CSharp.htm)
[Set Transparency of Components in Large Design Review (VB.NET)](Set_Transparency_of_Components_LDR_Mode_Example_VBNET.htm)
[Set Transparency of Components in Large Design Review (VBA)](Set_Transparency_of_Components_LDR_Mode_Example_VB.htm)

## Remarks

This property is valid only when the assembly is opened in Large Design Review mode, and one or more of its components have been modified. If this property is enabled, modified components are opaque, and unmodified components are transparent.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::LargeDesignReviewTransparencyLevel Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~LargeDesignReviewTransparencyLevel.html)
[IAssemblyDoc::LargeDesignReviewTransparencyLevelDynamic Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~LargeDesignReviewTransparencyLevelDynamic.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
