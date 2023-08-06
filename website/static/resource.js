document.addEventListener('DOMContentLoaded', function () {
    const resourceType = document.getElementById('resourceType');
    const resourceList = document.getElementById('resourceList');
    const specificResource = document.getElementById('specificResource');
    const resourceDetails = document.getElementById('resourceDetails');
    const content = document.getElementById('content');
    
    resourceType.addEventListener('change', function () {
        if (resourceType.value === 'select') {
            resourceList.classList.add('hidden');
            specificResource.disabled = true;
            resourceDetails.classList.add('hidden');
        } else {
            resourceList.classList.remove('hidden');
            specificResource.disabled = false;
            resourceDetails.classList.add('hidden');
        }
    });
    
    specificResource.addEventListener('change', function () {
        if (specificResource.value === 'select') {
            resourceDetails.classList.add('hidden');
        } else {
            // Simulate fetching resource details from the server
            const resource = specificResource.value;
            const details = `Details for ${resource}`;
            
            content.textContent = details;
            resourceDetails.classList.remove('hidden');
        }
    });
});
