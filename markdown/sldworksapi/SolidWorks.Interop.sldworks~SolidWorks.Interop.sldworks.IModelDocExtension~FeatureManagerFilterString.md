---
title: "FeatureManagerFilterString Property (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "FeatureManagerFilterString"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~FeatureManagerFilterString.html"
---

# FeatureManagerFilterString Property (IModelDocExtension)

Gets or sets the string in the FeatureManager design tree filter.

## Syntax

### Visual Basic (Declaration)

```vb
Property FeatureManagerFilterString As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim value As System.String

instance.FeatureManagerFilterString = value

value = instance.FeatureManagerFilterString
```

### C#

```csharp
System.string FeatureManagerFilterString {get; set;}
```

### C++/CLI

```cpp
property System.String^ FeatureManagerFilterString {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

String in FeatureManager design tree filter

## VBA Syntax

See [ModelDocExtension::FeatureManagerFilterString](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~FeatureManagerFilterString.html).

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
