---
title: "UseUpdateLoadDirection Property (ICWNonLinearStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWNonLinearStudyOptions"
member: "UseUpdateLoadDirection"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~UseUpdateLoadDirection.html"
---

# UseUpdateLoadDirection Property (ICWNonLinearStudyOptions)

Obsolete. Superseded by [ICWNonLinearStudyOptions::UseUpdateLoadDirection2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~UseUpdateLoadDirection2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property UseUpdateLoadDirection As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWNonLinearStudyOptions
Dim value As System.Integer

instance.UseUpdateLoadDirection = value

value = instance.UseUpdateLoadDirection
```

### C#

```csharp
System.int UseUpdateLoadDirection {get; set;}
```

### C++/CLI

```cpp
property System.int UseUpdateLoadDirection {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

- 1 = Use update load direction with deflection flag
- 0 = Do not use update load direction with deflection flag

## VBA Syntax

See [CWNonLinearStudyOptions::UseUpdateLoadDirection](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWNonLinearStudyOptions~UseUpdateLoadDirection.html).

## Examples

See the [ICWNonLinearStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html) examples.

## See Also

[ICWNonLinearStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html)
[ICWNonLinearStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
