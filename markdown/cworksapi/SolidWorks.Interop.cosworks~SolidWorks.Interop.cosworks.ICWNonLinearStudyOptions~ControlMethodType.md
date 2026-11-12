---
title: "ControlMethodType Property (ICWNonLinearStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWNonLinearStudyOptions"
member: "ControlMethodType"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~ControlMethodType.html"
---

# ControlMethodType Property (ICWNonLinearStudyOptions)

Gets or sets the type of control method.

## Syntax

### Visual Basic (Declaration)

```vb
Property ControlMethodType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWNonLinearStudyOptions
Dim value As System.Integer

instance.ControlMethodType = value

value = instance.ControlMethodType
```

### C#

```csharp
System.int ControlMethodType {get; set;}
```

### C++/CLI

```cpp
property System.int ControlMethodType {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Type of control method as defined in [swsNonLinearOptionControlMethodType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsNonLinearOptionControlMethodType_e.html)

## VBA Syntax

See [CWNonLinearStudyOptions::ControlMethodType](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWNonLinearStudyOptions~ControlMethodType.html).

## Examples

See the [ICWNonLinearStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html) examples.

## See Also

[ICWNonLinearStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html)
[ICWNonLinearStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2010 SP3.0
