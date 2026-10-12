---
title: "GetPLMID Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "GetPLMID"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetPLMID.html"
---

# GetPLMID Method (IModelDocExtension)

Gets the ID of this [SOLIDWORKS Design connected to the 3DEXPERIENCE platform](ms-its:sldworksapiprogguide.chm:://Overview/SOLIDWORKS_Connected.htm) document.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPLMID() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim value As System.String

value = instance.GetPLMID()
```

### C#

```csharp
System.string GetPLMID()
```

### C++/CLI

```cpp
System.String^ GetPLMID();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Document ID

## VBA Syntax

See [ModelDocExtension::GetPLMID](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~GetPLMID.html).

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

## Availability

SOLIDWORKS 2020 SP3.1, Revision Number 28.3.1
