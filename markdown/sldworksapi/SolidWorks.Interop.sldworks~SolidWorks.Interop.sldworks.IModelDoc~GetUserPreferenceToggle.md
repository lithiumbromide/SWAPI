---
title: "GetUserPreferenceToggle Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "GetUserPreferenceToggle"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~GetUserPreferenceToggle.html"
---

# GetUserPreferenceToggle Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::GetUserPreferenceToggle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetUserPreferenceToggle.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetUserPreferenceToggle( _
   ByVal UserPreferenceToggle As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim UserPreferenceToggle As System.Integer
Dim value As System.Boolean

value = instance.GetUserPreferenceToggle(UserPreferenceToggle)
```

### C#

```csharp
System.bool GetUserPreferenceToggle(
   System.int UserPreferenceToggle
)
```

### C++/CLI

```cpp
System.bool GetUserPreferenceToggle(
   System.int UserPreferenceToggle
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UserPreferenceToggle`:

## VBA Syntax

See [ModelDoc::GetUserPreferenceToggle](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~GetUserPreferenceToggle.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
