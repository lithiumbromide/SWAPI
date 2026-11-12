---
title: "TemplatePath Property (ISplitBodyFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISplitBodyFeatureData"
member: "TemplatePath"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~TemplatePath.html"
---

# TemplatePath Property (ISplitBodyFeatureData)

Gets or sets the template to use to make this Split feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property TemplatePath As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISplitBodyFeatureData
Dim value As System.String

instance.TemplatePath = value

value = instance.TemplatePath
```

### C#

```csharp
System.string TemplatePath {get; set;}
```

### C++/CLI

```cpp
property System.String^ TemplatePath {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Path and file name of the template

## VBA Syntax

See [SplitBodyFeatureData::TemplatePath](ms-its:sldworksapivb6.chm::/sldworks~SplitBodyFeatureData~TemplatePath.html).

## Remarks

Set this property only if [ISplitBodyFeatureData::OverrideDefaultTemplateSettings](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~OverrideDefaultTemplateSettings.html) is set to true.

## See Also

[ISplitBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData.html)
[ISplitBodyFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
