---
title: "IExternalReference Interface"
project: ""
interface: "IExternalReference"
member: ""
kind: "interface"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IExternalReference.html"
---

# IExternalReference Interface

Allows access to an external reference (e.g., referenced drawing).

## Syntax

### Visual Basic

```vb
Public Interface IExternalReference
```

### C#

```csharp
public interface IExternalReference
```

### JScript

```
public interface IExternalReference
```

### Managed Extensions for C++

```
public __gc __interface IExternalReference
```

### C++/CLI

```cpp
public interface class IExternalReference
```

## Examples

This code snippet shows how to get the external references and their names and paths.

##### COM native C++

_variant_t pVariantArray = dsDoc->GetExternalReferences();
if( V_VT( &pVariantArray ) != VT_EMPTY )
{
IExternalReferencePtr *ExtRef = NULL;
int countOfExtRef = 0;
[TypeConverter::convertVariantArrayToPtrArray](GettingStarted-draftsightapi.html#convertVariantArrayToPtrArray)<IExternalReferencePtr, IExternalReference>( pVariantArray, ExtRef, countOfExtRef );

if( ExtRef && countOfExtRef > 0)
{
for( int i = 0; i < countOfExtRef; ++i )
{
bstr_t blockName= ExtRef[i]->GetName();

bstr_t xRefPath = ExtRef[i]->GetPathName();

}
delete[] ExtRef;
}
}

## Examples

[Get and Set Block Definitions, Block Instances, and BlockAttribute Instances (C#)](Get_and_Set_Block_Definitions_Block_Instances_and_BlockAttribute_Instances_Example_CSharp.htm)
[Get and Set Block Definitions, Block Instances, and BlockAttribute Instances (VB.NET)](Get_and_Set_Block_Definitions_Block_Instances_and_BlockAttribute_Instances_Example_VBNET.htm)
[Get and Set Block Definitions, Block Instances, and BlockAttribute Instances (VBA)](Get_and_Set_Block_Definitions_Block_Instances_and_BlockAttribute_Instances_Example_VBA.htm)
[Insert External Reference (C#)](Insert_External_Reference_Example_CSharp.htm)
[Insert External Reference (VB.NET)](Insert_External_Reference_Example_VBNET.htm)
[Insert External Reference (VBA)](Insert_External_Reference_Example_VBA.htm)

## Accessors

[IBlockDefinition::GetExternalReference](Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition~GetExternalReference.html)

[IDocument::GetExternalReferences](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetExternalReferences.html)

[IExternalReference::GetChildren](Interop.dsAutomation~Interop.dsAutomation.IExternalReference~GetChildren.html)

[IExternalReference::GetParents](Interop.dsAutomation~Interop.dsAutomation.IExternalReference~GetParents.html)

## Access Diagram

DSObjectModel.pdf#ExternalReference

[ExternalReference](DSObjectModel.pdf#ExternalReference)

## See Also

[IExternalReference Members](Interop.dsAutomation~Interop.dsAutomation.IExternalReference_members.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[ISketchManager::DetachExternalReference Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~DetachExternalReference.html)
