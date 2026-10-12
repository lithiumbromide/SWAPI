---
title: "ConfigurationName Property (IDocumentSpecification)"
project: "SOLIDWORKS API Help"
interface: "IDocumentSpecification"
member: "ConfigurationName"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~ConfigurationName.html"
---

# ConfigurationName Property (IDocumentSpecification)

Gets or sets the name of the configuration to load when opening a model document.

## Syntax

### Visual Basic (Declaration)

```vb
Property ConfigurationName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IDocumentSpecification
Dim value As System.String

instance.ConfigurationName = value

value = instance.ConfigurationName
```

### C#

```csharp
System.string ConfigurationName {get; set;}
```

### C++/CLI

```cpp
property System.String^ ConfigurationName {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Name of configuration to load

## VBA Syntax

See [DocumentSpecification::ConfigurationName](ms-its:sldworksapivb6.chm::/sldworks~DocumentSpecification~ConfigurationName.html).

## Remarks

This property is not valid for opening **3D**EXPERIENCE files using [SOLIDWORKS Design connected to the 3DEXPERIENCE platform](ms-its:sldworksapiprogguide.chm:://Overview/SOLIDWORKS_Connected.htm).

## See Also

[IDocumentSpecification Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification.html)
[IDocumentSpecification Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
