---
title: "IntegrationMethodType Property (ICWNonLinearStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWNonLinearStudyOptions"
member: "IntegrationMethodType"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~IntegrationMethodType.html"
---

# IntegrationMethodType Property (ICWNonLinearStudyOptions)

Gets or sets the type of numerical integration method.

## Syntax

### Visual Basic (Declaration)

```vb
Property IntegrationMethodType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWNonLinearStudyOptions
Dim value As System.Integer

instance.IntegrationMethodType = value

value = instance.IntegrationMethodType
```

### C#

```csharp
System.int IntegrationMethodType {get; set;}
```

### C++/CLI

```cpp
property System.int IntegrationMethodType {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Type of numerical integration method as defined in [swsNonLinearOptionIntegrationMethodType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsNonLinearOptionIntegrationMethodType_e.html)

## VBA Syntax

See [CWNonLinearStudyOptions::IntegrationMethodType](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWNonLinearStudyOptions~IntegrationMethodType.html).

## Examples

See the [ICWNonLinearStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html) examples.

## See Also

[ICWNonLinearStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html)
[ICWNonLinearStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2010 SP3.0
