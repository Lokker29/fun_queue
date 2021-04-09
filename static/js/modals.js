$(document).ready(function () {
    $('.open-modal').click((eventObject) => {
        const modalSelector = eventObject.target.dataset.target;

        $(modalSelector).addClass('is-active');
    });

    const hideModal = (eventObject) => {
        const modal = $(eventObject.target).parents('.modal');
        modal.removeClass('is-active');

        clearForm($(modal).find('form'))
    };

    $('.modal-background').click(hideModal);
    $('.close-modal').click(hideModal);

    $('.ajax-modal').click((eventObject) => {
        eventObject.preventDefault();

        const form = $(eventObject.target).parents('.modal form');
        $.ajax({
            url: form.attr('action'),
            method: form.attr('method'),
            data: form.serialize(),
            beforeSend: (request) => {
                request.setRequestHeader("X-CSRFToken", $(form).find('input[name="csrfmiddlewaretoken"]').val());
            },
            success: (data) => {
                console.log(data);
                window.location.href = data.next;
            },
            error: (response) => {
                $(form).find('.field-error').remove();
                clearFormErrorCss(form);

                Object.entries(response.responseJSON.errors).forEach(([fieldName, errors]) => {
                    const field = $(form).find('#id_' + fieldName);

                    const errorElement = `<div class="is-size-7 has-text-danger field-error">${errors[0]}</div>`;

                    const selectDiv = field.parent('.select');

                    if (selectDiv.length !== 0) {
                        selectDiv.addClass('is-danger shake-horizontal');
                        selectDiv.append(errorElement);
                    } else {
                        field.addClass('is-danger shake-horizontal');
                        field.parents('.control').append(errorElement)
                    }
                })
            }
        })
    });

    const clearFormErrorCss = (form) => {
        form.find('.shake-horizontal.is-danger').removeClass('shake-horizontal is-danger');
        form.find('.field-error').remove();
    }

    const clearForm = (form) => {
        form.not(':button, :submit, :reset, :hidden')
            .val('')
            .prop('checked', false)
            .prop('selected', false);

        clearFormErrorCss(form);
    };
});
