---
title: "LargeDesignReviewMark Property (IConfiguration)"
project: "SOLIDWORKS API Help"
interface: "IConfiguration"
member: "LargeDesignReviewMark"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~LargeDesignReviewMark.html"
---

# LargeDesignReviewMark Property (IConfiguration)

Gets or sets whether to add display data to this configuration when the document is saved.

## Syntax

### Visual Basic (Declaration)

```vb
Property LargeDesignReviewMark As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IConfiguration
Dim value As System.Boolean

instance.LargeDesignReviewMark = value

value = instance.LargeDesignReviewMark
```

### C#

```csharp
System.bool LargeDesignReviewMark {get; set;}
```

### C++/CLI

```cpp
property System.bool LargeDesignReviewMark {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to add display data, false to not

## VBA Syntax

See [Configuration::LargeDesignReviewMark](ms-its:sldworksapivb6.chm::/sldworks~Configuration~LargeDesignReviewMark.html).

## Examples

[Get and Set Large Design Review Marks for Configurations (C#)](Get_and_Set_Large_Design_Review_Marks_for_Configurations_Example_CSharp.htm)
[Get and Set Large Design Review Marks for Configurations (VB.NET)](Get_and_Set_Large_Design_Review_Marks_for_Configurations_Example_VBNET.htm)
[Get and Set Large Design Review Marks for Configurations (VBA)](Get_and_Set_Large_Design_Review_Marks_for_Configurations_Example_VB.htm)

## Remarks

This property is valid only if this configuration is one of multiple configurations defined for the assembly or part.

Before SOLIDWORKS 2019, this property specified whether to generate a display list for the configuration of an assembly when it is saved. As of SOLIDWORKS 2019, this property specifies whether to generate a display list for this configuration of:

- an assembly on save. If this property is set to true, the assembly configuration's display list is saved, making the configuration visible in Large Design Review mode. In the user interface, this corresponds to selecting the assembly's **ConfigurationManager >** `configuration_name` **RMB menu > Add Display Data Mark**.

- or -

- a part on save. If this property is set to true, the part configuration's display list is saved, making the configuration visible in other applications, such as eDrawings. In the user interface, this corresponds to selecting the part's **ConfigurationManager >** `configuration_name` **RMB menu > Add Display Data Mark**.

## See Also

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.html)
[IDocumentSpecification::ViewOnly Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~ViewOnly.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
