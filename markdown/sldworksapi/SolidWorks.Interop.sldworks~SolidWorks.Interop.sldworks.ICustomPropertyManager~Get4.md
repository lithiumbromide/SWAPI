---
title: "Get4 Method (ICustomPropertyManager)"
project: "SOLIDWORKS API Help"
interface: "ICustomPropertyManager"
member: "Get4"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~Get4.html"
---

# Get4 Method (ICustomPropertyManager)

Obsolete. Superseded by [ICustomPropertyManager::Get5](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICustomPropertyManager~Get5.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function Get4( _
   ByVal FieldName As System.String, _
   ByVal UseCached As System.Boolean, _
   ByRef ValOut As System.String, _
   ByRef ResolvedValOut As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICustomPropertyManager
Dim FieldName As System.String
Dim UseCached As System.Boolean
Dim ValOut As System.String
Dim ResolvedValOut As System.String
Dim value As System.Boolean

value = instance.Get4(FieldName, UseCached, ValOut, ResolvedValOut)
```

### C#

```csharp
System.bool Get4(
   System.string FieldName,
   System.bool UseCached,
   out System.string ValOut,
   out System.string ResolvedValOut
)
```

### C++/CLI

```cpp
System.bool Get4(
   System.String^ FieldName,
   System.bool UseCached,
   [Out] System.String^ ValOut,
   [Out] System.String^ ResolvedValOut
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FieldName`: Name of the custom property
- `UseCached`: True if the configuration has been activated, false if not (see Remarks)
- `ValOut`: Value of the custom property
- `ResolvedValOut`: Evaluated value of the custom property

### Return Value

True if up-to-date data is returned, false if not (see Remarks)

## VBA Syntax

See [CustomPropertyManager::Get4](ms-its:sldworksapivb6.chm::/sldworks~CustomPropertyManager~Get4.html).

## Examples

[Get Custom Properties of Referenced Part (C#)](Get_Custom_Properties_of_Referenced_Part_Example_CSharp.htm)
[Get Custom Properties of Referenced Part (VB.NET)](Get_Custom_Properties_of_Referenced_Part_Example_VBNET.htm)
[Get Custom Properties of Referenced Part (VBA)](Get_Custom_Properties_of_Referenced_Part_Example_VB.htm)

## Remarks

This method can get the cached custom property, even if the configuration is not currently active, without having to change configurations.

| If UseCached is set to... | And the configuration has already been activated... | Then... |
| --- | --- | --- |
| True | Yes | Up-to-date data is returned and return value = true |
| True | No | Cached data is returned and return value = false |
| False | Yes | Up-to-date data is returned and return value = true |
| False | No | Up-to-date data is returned and return value = true |

This method returns configuration-specific, linked, custom-property, evaluated data more quickly than the now obsolete [ICustomPropertyManager::Get2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICustomPropertyManager~Get2.html), if the configuration was previously activated.

If you always want up-to-date data, then you should set UseCached to false. This might result in a more time-consuming call if the configuration was not previously activated.

This method does not preface the resolved evaluated values of external referenced documents with **fromparent+**, unlike the now obsolete [ICustomPropertyManager::Get3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICustomPropertyManager~Get3.html).

## See Also

[ICustomPropertyManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager.html)
[ICustomPropertyManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager_members.html)

## Availability

SOLIDWORKS 2011 SP4, Revision Number 19.4
