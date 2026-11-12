---
title: "Configuration Property (IWeldmentCutListFeature)"
project: "SOLIDWORKS API Help"
interface: "IWeldmentCutListFeature"
member: "Configuration"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature~Configuration.html"
---

# Configuration Property (IWeldmentCutListFeature)

Gets or sets the name of the configuration for this weldment cut list table.

## Syntax

### Visual Basic (Declaration)

```vb
Property Configuration As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IWeldmentCutListFeature
Dim value As System.String

instance.Configuration = value

value = instance.Configuration
```

### C#

```csharp
System.string Configuration {get; set;}
```

### C++/CLI

```cpp
property System.String^ Configuration {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Name of the configuration shown in the weldment cut list table

## VBA Syntax

See [WeldmentCutListFeature::Configuration](ms-its:sldworksapivb6.chm::/sldworks~WeldmentCutListFeature~Configuration.html).

## Examples

See the [IWeldmentCutListFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature.html) examples.

## See Also

[IWeldmentCutListFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature.html)
[IWeldmentCutListFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
