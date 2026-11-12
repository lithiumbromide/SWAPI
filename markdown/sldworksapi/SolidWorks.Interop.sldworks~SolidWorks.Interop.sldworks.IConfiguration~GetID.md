---
title: "GetID Method (IConfiguration)"
project: "SOLIDWORKS API Help"
interface: "IConfiguration"
member: "GetID"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetID.html"
---

# GetID Method (IConfiguration)

Gets the configuration ID of this configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetID() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IConfiguration
Dim value As System.Integer

value = instance.GetID()
```

### C#

```csharp
System.int GetID()
```

### C++/CLI

```cpp
System.int GetID();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Configuration ID of this configuration

## VBA Syntax

See [Configuration::GetID](ms-its:sldworksapivb6.chm::/sldworks~Configuration~GetID.html).

## Examples

[Get ID of Active Configuration or Current Drawing Sheet (VB.NET)](Get_ID_of_Active_Configuration_or_Current_Drawing_Sheet_Example_VBNET.htm)
[GEt ID of Active Configuration or Current Drawing Sheet (VBA)](Get_ID_of_Active_Configuration_or_Current_Drawing_Sheet_Example_VB.htm)
[Get ID of Active Configuration or Current Drawing Sheet (C#)](Get_ID_of_Active_Configuration_or_Current_Drawing_Sheet_Example_CSharp.htm)

## Remarks

A configuration ID:

- is unique within the document.
- is persistent across SOLIDWORKS Design sessions and never changes, even if you [change the name of the configuration](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~Name.html).
- can be used to identify a specific configuration when multiple configurations exist in a model.
- cannot be assigned by users.
- is not the same as a [persistent reference ID](sldworksapiprogguide.chm::/overview/Persistent_Reference_IDs.htm). You can get a configuration using its persistent reference ID, but you cannot get a configuration using this method.

## See Also

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
