---
title: "GetRepresentationParent Method (IConfiguration)"
project: "SOLIDWORKS API Help"
interface: "IConfiguration"
member: "GetRepresentationParent"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetRepresentationParent.html"
---

# GetRepresentationParent Method (IConfiguration)

Gets the Physical Product represented by this configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRepresentationParent() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IConfiguration
Dim value As System.String

value = instance.GetRepresentationParent()
```

### C#

```csharp
System.string GetRepresentationParent()
```

### C++/CLI

```cpp
System.String^ GetRepresentationParent();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Physical Product/Family member name

## VBA Syntax

See [Configuration::GetRepresentationParent](ms-its:sldworksapivb6.chm::/sldworks~Configuration~GetRepresentationParent.html).

## Remarks

This method is valid only:

- For [SOLIDWORKS Design connected to the 3DEXPERIENCE platform](ms-its:sldworksapiprogguide.chm:://Overview/SOLIDWORKS_Connected.htm)

- and -

- If [IConfiguration::Get3DExperienceType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~Get3DExperienceType.html) is not 0

## See Also

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.html)

## Availability

SOLIDWORKS 2020 SP3.1, Revision Number 28.3.1
