---
title: "Get5 Method (ICustomPropertyManager)"
project: "SOLIDWORKS API Help"
interface: "ICustomPropertyManager"
member: "Get5"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~Get5.html"
---

# Get5 Method (ICustomPropertyManager)

Obsolete. Superseded by [ICustomPropertyManager::Get6](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~Get6.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function Get5( _
   ByVal FieldName As System.String, _
   ByVal UseCached As System.Boolean, _
   ByRef ValOut As System.String, _
   ByRef ResolvedValOut As System.String, _
   ByRef WasResolved As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICustomPropertyManager
Dim FieldName As System.String
Dim UseCached As System.Boolean
Dim ValOut As System.String
Dim ResolvedValOut As System.String
Dim WasResolved As System.Boolean
Dim value As System.Integer

value = instance.Get5(FieldName, UseCached, ValOut, ResolvedValOut, WasResolved)
```

### C#

```csharp
System.int Get5(
   System.string FieldName,
   System.bool UseCached,
   out System.string ValOut,
   out System.string ResolvedValOut,
   out System.bool WasResolved
)
```

### C++/CLI

```cpp
System.int Get5(
   System.String^ FieldName,
   System.bool UseCached,
   [Out] System.String^ ValOut,
   [Out] System.String^ ResolvedValOut,
   [Out] System.bool WasResolved
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FieldName`: Name of the custom property
- `UseCached`: True if the configuration has been activated, false if not (see Remarks)
- `ValOut`: Value of the custom property
- `ResolvedValOut`: Evaluated value of the custom property
- `WasResolved`: True if the value was evaluated, false if not (see **Remarks**)

### Return Value

Result code as defined in [swCustomInfoGetResult_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCustomInfoGetResult_e.html)

## VBA Syntax

See [CustomPropertyManager::Get5](ms-its:sldworksapivb6.chm::/sldworks~CustomPropertyManager~Get5.html).

## Remarks

This method returns configuration-specific, linked, and evaluated custom-property data more quickly than the now obsolete ICustomPropertyManager::Get2, if the configuration is previously activated.

This method gets the cached custom property, even if its configuration is not currently active.

| If UseCached is set to... | And the configuration has already been activated... | Then... |
| --- | --- | --- |
| True | Yes | Up-to-date data is returned and WasResolved = true |
| True | No | Cached data is returned and WasResolved = false |
| False | Yes | Up-to-date data is returned and WasResolved = true |
| False | No | Up-to-date data is returned and WasResolved = true |

If you always want up-to-date data, then you should set UseCached to false.

If the configuration is not previously activated, this method might take longer, as it loops through all of the model's configurations to find the specified custom property. When it finishes, the model might not be in its original configuration. To return the model to its original configuration, call [IModelDoc2::ForceRebuild3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ForceRebuild3.html) after calling this method.

This method does not preface the resolved evaluated values of external referenced documents with fromparent+, unlike the now obsolete ICustomPropertyManager::Get3.

## See Also

[ICustomPropertyManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager.html)
[ICustomPropertyManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager_members.html)
[ICustomPropertyManager::GetAll2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~GetAll2.html)
[ICustomPropertyManager::GetNames Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~GetNames.html)
[ICustomPropertyManager::GetType2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~GetType2.html)
[ICustomPropertyManager::IGetNames Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~IGetNames.html)
[ICustomPropertyManager::Set2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~Set2.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
