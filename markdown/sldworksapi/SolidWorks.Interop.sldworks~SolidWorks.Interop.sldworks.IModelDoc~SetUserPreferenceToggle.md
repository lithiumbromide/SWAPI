---
title: "SetUserPreferenceToggle Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "SetUserPreferenceToggle"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SetUserPreferenceToggle.html"
---

# SetUserPreferenceToggle Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::SetUserPreferenceToggle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SetUserPreferenceToggle.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetUserPreferenceToggle( _
   ByVal UserPreferenceValue As System.Integer, _
   ByVal OnFlag As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim UserPreferenceValue As System.Integer
Dim OnFlag As System.Boolean
Dim value As System.Boolean

value = instance.SetUserPreferenceToggle(UserPreferenceValue, OnFlag)
```

### C#

```csharp
System.bool SetUserPreferenceToggle(
   System.int UserPreferenceValue,
   System.bool OnFlag
)
```

### C++/CLI

```cpp
System.bool SetUserPreferenceToggle(
   System.int UserPreferenceValue,
   System.bool OnFlag
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UserPreferenceValue`:
- `OnFlag`:

## VBA Syntax

See [ModelDoc::SetUserPreferenceToggle](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~SetUserPreferenceToggle.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
