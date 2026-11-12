---
title: "OverrideDefaultTemplateSettings Property (ISplitBodyFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISplitBodyFeatureData"
member: "OverrideDefaultTemplateSettings"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~OverrideDefaultTemplateSettings.html"
---

# OverrideDefaultTemplateSettings Property (ISplitBodyFeatureData)

Gets or sets whether to use an alternate template to apply to all new part or assembly files created during the split operation.

## Syntax

### Visual Basic (Declaration)

```vb
Property OverrideDefaultTemplateSettings As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISplitBodyFeatureData
Dim value As System.Boolean

instance.OverrideDefaultTemplateSettings = value

value = instance.OverrideDefaultTemplateSettings
```

### C#

```csharp
System.bool OverrideDefaultTemplateSettings {get; set;}
```

### C++/CLI

```cpp
property System.bool OverrideDefaultTemplateSettings {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to use an alternate template, false to use the default template

## VBA Syntax

See [SplitBodyFeatureData::OverrideDefaultTemplateSettings](ms-its:sldworksapivb6.chm::/sldworks~SplitBodyFeatureData~OverrideDefaultTemplateSettings.html).

## Remarks

Use [ISplitBodyFeatureData::TemplatePath](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~TemplatePath.html) to specify the alternate template.

## See Also

[ISplitBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData.html)
[ISplitBodyFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
